# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-11T04:52:28.883790+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0068` n `13`; crypto_alt avg `0.1534` n `235`; crypto_major avg `0.0788` n `8`; equity avg `0.0033` n `150`; fx avg `0.0044` n `6`; index avg `0.0001` n `26`; metal avg `-0.0018` n `20`; unknown avg `0.0309` n `1117`
- 1h: commodity avg `0.0092` n `13`; crypto_alt avg `0.5748` n `235`; crypto_major avg `0.3351` n `8`; equity avg `0.0284` n `150`; fx avg `0.0052` n `6`; index avg `0.0048` n `26`; metal avg `-0.0055` n `20`; unknown avg `0.0274` n `1109`
- 4h: commodity avg `0.0971` n `13`; crypto_alt avg `-0.1601` n `235`; crypto_major avg `-0.0265` n `8`; equity avg `-0.0714` n `150`; fx avg `0.0071` n `6`; index avg `-0.0175` n `26`; metal avg `-0.0049` n `20`; unknown avg `-0.3359` n `1109`
- 24h: commodity avg `0.1713` n `13`; crypto_alt avg `0.5011` n `235`; crypto_major avg `0.1075` n `8`; equity avg `-0.0396` n `150`; fx avg `-0.0074` n `6`; index avg `-0.0371` n `26`; metal avg `-0.0123` n `20`; unknown avg `0.2309` n `942`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1546`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1429`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.12`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1163`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1004`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0851`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
