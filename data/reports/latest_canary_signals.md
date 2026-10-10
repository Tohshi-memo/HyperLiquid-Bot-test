# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T05:52:32.783616+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0069` n `13`; crypto_alt avg `-0.0055` n `235`; crypto_major avg `-0.0108` n `8`; equity avg `-0.0005` n `150`; fx avg `0.0` n `6`; index avg `-0.0016` n `26`; metal avg `0.0056` n `20`; unknown avg `-0.2515` n `1116`
- 1h: commodity avg `0.0118` n `13`; crypto_alt avg `0.2962` n `235`; crypto_major avg `0.246` n `8`; equity avg `0.0003` n `150`; fx avg `-0.0008` n `6`; index avg `0.0031` n `26`; metal avg `-0.0095` n `20`; unknown avg `-0.1918` n `1114`
- 4h: commodity avg `0.0161` n `13`; crypto_alt avg `0.5257` n `235`; crypto_major avg `0.1799` n `8`; equity avg `0.0334` n `150`; fx avg `0.0055` n `6`; index avg `0.0106` n `26`; metal avg `-0.0072` n `20`; unknown avg `-0.3784` n `1108`
- 24h: commodity avg `0.0564` n `13`; crypto_alt avg `2.139` n `235`; crypto_major avg `0.3841` n `8`; equity avg `0.066` n `150`; fx avg `-0.043` n `6`; index avg `0.0402` n `26`; metal avg `0.0465` n `20`; unknown avg `12.6758` n `902`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1012`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0992`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0926`, n `668`, weak_sample_signal
