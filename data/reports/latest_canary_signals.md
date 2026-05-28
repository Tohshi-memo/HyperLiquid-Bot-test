# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-28T14:37:26.524569+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.3956` n `12`; crypto_alt avg `-0.1191` n `228`; crypto_major avg `-0.3148` n `8`; equity avg `0.1852` n `67`; fx avg `0.0028` n `6`; index avg `0.042` n `23`; metal avg `-0.0282` n `18`; unknown avg `-0.0376` n `419`
- 1h: commodity avg `-0.2357` n `12`; crypto_alt avg `0.0572` n `228`; crypto_major avg `0.3513` n `8`; equity avg `0.9193` n `67`; fx avg `-0.0245` n `6`; index avg `0.3607` n `23`; metal avg `0.8362` n `18`; unknown avg `-0.1174` n `419`
- 4h: commodity avg `0.3625` n `12`; crypto_alt avg `-0.5368` n `228`; crypto_major avg `-0.1571` n `8`; equity avg `1.1424` n `67`; fx avg `0.0807` n `6`; index avg `0.5488` n `23`; metal avg `0.8246` n `18`; unknown avg `-0.368` n `419`
- 24h: commodity avg `0.4295` n `12`; crypto_alt avg `-4.9203` n `228`; crypto_major avg `-2.7838` n `8`; equity avg `0.2461` n `67`; fx avg `-0.0319` n `6`; index avg `0.3814` n `23`; metal avg `-0.3867` n `18`; unknown avg `-1.6204` n `408`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1941`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1818`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1799`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1648`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1554`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.153`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1432`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.143`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
