# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-20T10:22:26.298311+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0293` n `12`; crypto_alt avg `-0.0927` n `228`; crypto_major avg `-0.1417` n `8`; equity avg `-0.0368` n `78`; fx avg `0.0095` n `6`; index avg `-0.0133` n `23`; metal avg `-0.0043` n `18`; unknown avg `-0.0178` n `687`
- 1h: commodity avg `-0.0043` n `12`; crypto_alt avg `0.1446` n `228`; crypto_major avg `0.1984` n `8`; equity avg `-0.0341` n `78`; fx avg `0.3013` n `6`; index avg `-0.0046` n `23`; metal avg `-0.0091` n `18`; unknown avg `0.0676` n `687`
- 4h: commodity avg `-0.0238` n `12`; crypto_alt avg `0.1045` n `228`; crypto_major avg `-0.096` n `8`; equity avg `-0.1488` n `78`; fx avg `0.0266` n `6`; index avg `-0.0272` n `23`; metal avg `0.0149` n `18`; unknown avg `-0.1653` n `679`
- 24h: commodity avg `0.4954` n `12`; crypto_alt avg `-2.8287` n `228`; crypto_major avg `-3.3134` n `8`; equity avg `1.209` n `78`; fx avg `-0.0792` n `6`; index avg `0.2922` n `23`; metal avg `-4.1131` n `18`; unknown avg `0.0554` n `530`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0942`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0615`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0568`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0566`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.056`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
