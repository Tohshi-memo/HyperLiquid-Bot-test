# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T10:22:24.200782+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.1825` n `12`; crypto_alt avg `-0.1072` n `228`; crypto_major avg `-0.1086` n `8`; equity avg `-0.107` n `72`; fx avg `-0.0167` n `6`; index avg `-0.0086` n `23`; metal avg `-0.0791` n `18`; unknown avg `-0.1123` n `420`
- 1h: commodity avg `0.148` n `12`; crypto_alt avg `0.5242` n `228`; crypto_major avg `0.298` n `8`; equity avg `-0.0253` n `72`; fx avg `0.0117` n `6`; index avg `0.0058` n `23`; metal avg `0.113` n `18`; unknown avg `-0.1658` n `420`
- 4h: commodity avg `0.8811` n `12`; crypto_alt avg `0.4967` n `228`; crypto_major avg `0.1216` n `8`; equity avg `-0.2939` n `72`; fx avg `-0.0245` n `6`; index avg `0.0372` n `23`; metal avg `-0.1199` n `18`; unknown avg `-0.1831` n `420`
- 24h: commodity avg `1.8676` n `12`; crypto_alt avg `-0.886` n `228`; crypto_major avg `-3.0073` n `8`; equity avg `0.4099` n `72`; fx avg `0.049` n `6`; index avg `0.8176` n `23`; metal avg `-1.2301` n `18`; unknown avg `0.1031` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0689`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0556`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0522`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0499`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0411`, n `668`, weak_sample_signal
