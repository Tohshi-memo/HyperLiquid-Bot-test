# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-09T09:07:27.823228+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0023` n `13`; crypto_alt avg `0.1732` n `239`; crypto_major avg `0.1468` n `8`; equity avg `0.0762` n `158`; fx avg `0.0008` n `6`; index avg `0.033` n `27`; metal avg `0.0332` n `20`; unknown avg `153.1478` n `1259`
- 1h: commodity avg `0.026` n `13`; crypto_alt avg `1.6339` n `239`; crypto_major avg `1.3371` n `8`; equity avg `0.8653` n `158`; fx avg `0.0696` n `6`; index avg `0.1321` n `27`; metal avg `0.1023` n `20`; unknown avg `159.8795` n `1211`
- 4h: commodity avg `-0.2931` n `13`; crypto_alt avg `0.1491` n `239`; crypto_major avg `-0.2057` n `8`; equity avg `-0.4986` n `158`; fx avg `0.0315` n `6`; index avg `-0.0736` n `27`; metal avg `-0.1898` n `20`; unknown avg `173.7748` n `1109`
- 24h: commodity avg `-0.2064` n `13`; crypto_alt avg `-1.8398` n `239`; crypto_major avg `-2.9512` n `8`; equity avg `-0.5066` n `158`; fx avg `-0.079` n `6`; index avg `-0.0346` n `27`; metal avg `0.2776` n `20`; unknown avg `0.9986` n `948`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1789`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1618`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1187`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1134`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
