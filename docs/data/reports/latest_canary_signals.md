# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-03T22:22:31.171950+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0053` n `12`; crypto_alt avg `0.007` n `230`; crypto_major avg `0.0278` n `8`; equity avg `0.0392` n `103`; fx avg `0.0006` n `6`; index avg `0.0101` n `25`; metal avg `0.0179` n `20`; unknown avg `0.0056` n `784`
- 1h: commodity avg `-0.051` n `12`; crypto_alt avg `-0.2105` n `230`; crypto_major avg `-0.3022` n `8`; equity avg `0.1747` n `103`; fx avg `0.0224` n `6`; index avg `0.0452` n `25`; metal avg `-0.0422` n `20`; unknown avg `0.3377` n `784`
- 4h: commodity avg `0.0088` n `12`; crypto_alt avg `-0.3112` n `230`; crypto_major avg `-0.5929` n `8`; equity avg `0.3302` n `103`; fx avg `0.0615` n `6`; index avg `0.0766` n `25`; metal avg `0.112` n `20`; unknown avg `0.2617` n `784`
- 24h: commodity avg `0.035` n `12`; crypto_alt avg `-0.0678` n `230`; crypto_major avg `-0.4282` n `8`; equity avg `2.1428` n `103`; fx avg `-0.299` n `6`; index avg `0.1315` n `25`; metal avg `-0.2943` n `20`; unknown avg `-0.022` n `766`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.135`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0968`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0838`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0825`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0798`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0797`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
