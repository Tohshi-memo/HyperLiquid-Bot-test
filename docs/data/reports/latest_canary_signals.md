# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T20:37:27.879186+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.006` n `12`; crypto_alt avg `-0.0758` n `231`; crypto_major avg `0.0005` n `8`; equity avg `0.0047` n `127`; fx avg `-0.0127` n `6`; index avg `0.0028` n `26`; metal avg `0.0087` n `20`; unknown avg `-0.0749` n `793`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.0122` n `231`; crypto_major avg `-0.1259` n `8`; equity avg `0.0122` n `127`; fx avg `-0.0172` n `6`; index avg `-0.0184` n `26`; metal avg `-0.0586` n `20`; unknown avg `-0.2305` n `793`
- 4h: commodity avg `0.0399` n `12`; crypto_alt avg `-0.1555` n `231`; crypto_major avg `-0.8422` n `8`; equity avg `-0.1176` n `127`; fx avg `-0.037` n `6`; index avg `-0.0556` n `26`; metal avg `-0.1839` n `20`; unknown avg `0.1197` n `793`
- 24h: commodity avg `-0.1072` n `12`; crypto_alt avg `-3.2779` n `231`; crypto_major avg `-3.6783` n `8`; equity avg `-2.3184` n `127`; fx avg `-0.1335` n `6`; index avg `-0.1954` n `26`; metal avg `-0.3883` n `20`; unknown avg `-0.6607` n `760`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1169`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0972`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
