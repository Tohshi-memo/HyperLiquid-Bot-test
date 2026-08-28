# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T02:22:24.641715+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.3332` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0303` n `12`; crypto_alt avg `-0.7345` n `231`; crypto_major avg `-0.4415` n `8`; equity avg `-0.0417` n `127`; fx avg `0.0022` n `6`; index avg `0.0076` n `26`; metal avg `0.0149` n `20`; unknown avg `0.0748` n `792`
- 1h: commodity avg `0.018` n `12`; crypto_alt avg `-1.6082` n `231`; crypto_major avg `-1.3119` n `8`; equity avg `-0.0022` n `127`; fx avg `-0.007` n `6`; index avg `0.0213` n `26`; metal avg `-0.147` n `20`; unknown avg `1.1535` n `792`
- 4h: commodity avg `0.014` n `12`; crypto_alt avg `-0.9292` n `231`; crypto_major avg `-0.918` n `8`; equity avg `0.1427` n `127`; fx avg `-0.045` n `6`; index avg `0.0753` n `26`; metal avg `-0.1706` n `20`; unknown avg `-0.001` n `792`
- 24h: commodity avg `0.3717` n `12`; crypto_alt avg `0.6763` n `231`; crypto_major avg `1.7331` n `8`; equity avg `0.2352` n `127`; fx avg `-0.0015` n `6`; index avg `0.0564` n `26`; metal avg `-0.2224` n `20`; unknown avg `0.6585` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1297`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1224`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0789`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0674`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0594`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0587`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0559`, n `668`, weak_sample_signal
