# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T10:37:27.555146+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.0282` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0654` n `12`; crypto_alt avg `-0.7754` n `231`; crypto_major avg `-0.7571` n `8`; equity avg `-0.1169` n `127`; fx avg `0.0001` n `6`; index avg `-0.0063` n `26`; metal avg `-0.0232` n `20`; unknown avg `0.056` n `792`
- 1h: commodity avg `0.0938` n `12`; crypto_alt avg `-1.2889` n `231`; crypto_major avg `-1.0591` n `8`; equity avg `-0.2014` n `127`; fx avg `-0.0027` n `6`; index avg `-0.0309` n `26`; metal avg `-0.0212` n `20`; unknown avg `0.2116` n `792`
- 4h: commodity avg `0.227` n `12`; crypto_alt avg `0.4068` n `231`; crypto_major avg `0.8993` n `8`; equity avg `0.557` n `127`; fx avg `-0.0046` n `6`; index avg `0.0504` n `26`; metal avg `-0.2185` n `20`; unknown avg `0.1273` n `791`
- 24h: commodity avg `0.5554` n `12`; crypto_alt avg `0.665` n `231`; crypto_major avg `1.2481` n `8`; equity avg `1.8063` n `127`; fx avg `-0.0695` n `6`; index avg `0.2826` n `26`; metal avg `-0.4438` n `20`; unknown avg `0.4334` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1048`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.09`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0887`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0773`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0667`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0659`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0657`, n `668`, weak_sample_signal
