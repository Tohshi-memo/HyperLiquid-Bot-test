# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T00:37:24.245593+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.019` n `13`; crypto_alt avg `-0.0917` n `235`; crypto_major avg `-0.0661` n `8`; equity avg `-0.1222` n `150`; fx avg `0.0254` n `6`; index avg `-0.031` n `26`; metal avg `0.0011` n `20`; unknown avg `1.5635` n `1077`
- 1h: commodity avg `0.048` n `13`; crypto_alt avg `0.112` n `235`; crypto_major avg `-0.0238` n `8`; equity avg `-0.1293` n `150`; fx avg `-0.0529` n `6`; index avg `-0.0596` n `26`; metal avg `-0.0531` n `20`; unknown avg `0.1835` n `1069`
- 4h: commodity avg `0.0595` n `13`; crypto_alt avg `0.9042` n `235`; crypto_major avg `0.1877` n `8`; equity avg `0.0731` n `150`; fx avg `-0.0343` n `6`; index avg `-0.0081` n `26`; metal avg `-0.0181` n `20`; unknown avg `0.0464` n `1061`
- 24h: commodity avg `0.3752` n `13`; crypto_alt avg `-3.2321` n `235`; crypto_major avg `-3.2165` n `8`; equity avg `-1.5923` n `150`; fx avg `-0.2079` n `6`; index avg `-0.2935` n `26`; metal avg `-0.6925` n `20`; unknown avg `247.7727` n `980`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0809`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0684`, n `668`, weak_sample_signal
