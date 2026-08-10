# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T15:22:30.876029+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0355` n `12`; crypto_alt avg `-0.3607` n `230`; crypto_major avg `-0.4323` n `8`; equity avg `-0.1962` n `113`; fx avg `-0.0062` n `6`; index avg `-0.0206` n `25`; metal avg `-0.0241` n `20`; unknown avg `1.7939` n `784`
- 1h: commodity avg `0.1137` n `12`; crypto_alt avg `-0.6316` n `230`; crypto_major avg `-0.5991` n `8`; equity avg `-0.4249` n `113`; fx avg `0.0106` n `6`; index avg `-0.0418` n `25`; metal avg `0.1009` n `20`; unknown avg `1.9259` n `784`
- 4h: commodity avg `0.4824` n `12`; crypto_alt avg `-0.735` n `230`; crypto_major avg `-0.9542` n `8`; equity avg `-0.6852` n `113`; fx avg `0.0378` n `6`; index avg `-0.0309` n `25`; metal avg `0.1411` n `20`; unknown avg `1.0316` n `784`
- 24h: commodity avg `1.0518` n `12`; crypto_alt avg `-0.4125` n `230`; crypto_major avg `-1.3119` n `8`; equity avg `-1.2647` n `113`; fx avg `0.2479` n `6`; index avg `-0.0402` n `25`; metal avg `-0.079` n `20`; unknown avg `103.5386` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1633`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1593`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1534`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1421`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.138`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1345`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
