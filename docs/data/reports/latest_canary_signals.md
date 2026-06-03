# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-03T03:52:20.321056+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.41` - Polymarket crypto volume is unusually high.
- 1h_index_leads_crypto: score `1.3016` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_index_leads_crypto: score `1.2387` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0138` n `12`; crypto_alt avg `-0.5916` n `228`; crypto_major avg `-0.3055` n `8`; equity avg `-0.0375` n `72`; fx avg `0.0002` n `6`; index avg `0.0054` n `23`; metal avg `-0.0074` n `18`; unknown avg `1.2443` n `420`
- 1h: commodity avg `-0.0413` n `12`; crypto_alt avg `-1.242` n `228`; crypto_major avg `-1.2152` n `8`; equity avg `0.0349` n `72`; fx avg `-0.009` n `6`; index avg `0.0864` n `23`; metal avg `0.2131` n `18`; unknown avg `0.5466` n `420`
- 4h: commodity avg `-0.1162` n `12`; crypto_alt avg `-0.2107` n `228`; crypto_major avg `-1.004` n `8`; equity avg `0.1241` n `72`; fx avg `0.0615` n `6`; index avg `0.2347` n `23`; metal avg `0.2292` n `18`; unknown avg `-0.6108` n `419`
- 24h: commodity avg `0.7734` n `12`; crypto_alt avg `-5.6457` n `228`; crypto_major avg `-7.1343` n `8`; equity avg `1.2702` n `72`; fx avg `0.0378` n `6`; index avg `1.6275` n `23`; metal avg `0.0668` n `18`; unknown avg `0.0258` n `409`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.13`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1042`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.084`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0625`, n `668`, weak_sample_signal
