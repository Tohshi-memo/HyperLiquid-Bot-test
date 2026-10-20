# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-20T06:07:31.486297+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1031` n `13`; crypto_alt avg `-0.4368` n `237`; crypto_major avg `-0.2559` n `8`; equity avg `-0.2003` n `151`; fx avg `0.0095` n `6`; index avg `-0.0338` n `26`; metal avg `-0.0209` n `20`; unknown avg `2.7695` n `1176`
- 1h: commodity avg `0.1165` n `13`; crypto_alt avg `-0.5228` n `237`; crypto_major avg `-0.5051` n `8`; equity avg `-0.2672` n `151`; fx avg `-0.0041` n `6`; index avg `-0.0202` n `26`; metal avg `-0.1184` n `20`; unknown avg `7.625` n `1176`
- 4h: commodity avg `0.1545` n `13`; crypto_alt avg `0.1876` n `237`; crypto_major avg `0.1131` n `8`; equity avg `-0.5633` n `151`; fx avg `-0.0013` n `6`; index avg `-0.1089` n `26`; metal avg `-0.0207` n `20`; unknown avg `4.2148` n `1168`
- 24h: commodity avg `0.4432` n `13`; crypto_alt avg `-0.4574` n `237`; crypto_major avg `-0.9754` n `8`; equity avg `-1.9061` n `151`; fx avg `-0.004` n `6`; index avg `-0.3166` n `26`; metal avg `-0.3807` n `20`; unknown avg `5.3938` n `1010`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.202`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1513`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1145`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0767`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0711`, n `668`, weak_sample_signal
