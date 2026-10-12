# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T06:22:29.240603+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0455` n `13`; crypto_alt avg `-0.1313` n `235`; crypto_major avg `-0.1387` n `8`; equity avg `-0.0596` n `151`; fx avg `-0.0065` n `6`; index avg `0.0006` n `26`; metal avg `-0.0166` n `20`; unknown avg `0.1141` n `1133`
- 1h: commodity avg `0.1312` n `13`; crypto_alt avg `-0.6398` n `235`; crypto_major avg `-0.4905` n `8`; equity avg `-0.2942` n `151`; fx avg `-0.0014` n `6`; index avg `-0.0438` n `26`; metal avg `0.0028` n `20`; unknown avg `0.1692` n `1103`
- 4h: commodity avg `0.2164` n `13`; crypto_alt avg `0.2717` n `235`; crypto_major avg `0.0878` n `8`; equity avg `-0.9444` n `151`; fx avg `-0.0039` n `6`; index avg `-0.0879` n `26`; metal avg `-0.1835` n `20`; unknown avg `0.1687` n `1023`
- 24h: commodity avg `-0.2772` n `13`; crypto_alt avg `2.653` n `235`; crypto_major avg `1.551` n `8`; equity avg `-0.5331` n `151`; fx avg `-0.053` n `6`; index avg `-0.0498` n `26`; metal avg `0.0512` n `20`; unknown avg `0.564` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2008`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1726`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1237`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1087`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0763`, n `668`, weak_sample_signal
