# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T17:22:25.516682+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1129` n `12`; crypto_alt avg `-0.6937` n `228`; crypto_major avg `-0.815` n `8`; equity avg `-0.0423` n `74`; fx avg `0.0007` n `6`; index avg `-0.2811` n `23`; metal avg `-0.0708` n `18`; unknown avg `0.7063` n `424`
- 1h: commodity avg `-0.2077` n `12`; crypto_alt avg `0.1235` n `228`; crypto_major avg `-0.6904` n `8`; equity avg `-0.5288` n `74`; fx avg `-0.0003` n `6`; index avg `-0.6392` n `23`; metal avg `0.1657` n `18`; unknown avg `0.1426` n `424`
- 4h: commodity avg `-1.1412` n `12`; crypto_alt avg `-2.0989` n `228`; crypto_major avg `-2.7976` n `8`; equity avg `-3.6908` n `74`; fx avg `-0.1801` n `6`; index avg `-2.3087` n `23`; metal avg `-2.3585` n `18`; unknown avg `-1.04` n `424`
- 24h: commodity avg `-1.5453` n `12`; crypto_alt avg `-7.8377` n `228`; crypto_major avg `-6.1358` n `8`; equity avg `-5.9694` n `74`; fx avg `-0.0455` n `6`; index avg `-3.4199` n `23`; metal avg `-3.8534` n `18`; unknown avg `-1.8854` n `404`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0605`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0595`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
