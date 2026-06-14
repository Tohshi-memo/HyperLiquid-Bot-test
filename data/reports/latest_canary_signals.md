# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T22:07:33.267860+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `3.2635` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 1h_commodity_crypto_divergence: score `2.853` - Commodity perps and crypto are moving differently; check macro-linked stress.
- polymarket_volume_spike: score `2.26` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.4518` n `12`; crypto_alt avg `-0.6849` n `228`; crypto_major avg `-0.8362` n `8`; equity avg `-0.0846` n `74`; fx avg `0.0678` n `6`; index avg `-0.0949` n `23`; metal avg `1.2695` n `18`; unknown avg `-0.3553` n `645`
- 1h: commodity avg `-0.8698` n `12`; crypto_alt avg `1.9972` n `228`; crypto_major avg `1.9832` n `8`; equity avg `1.0926` n `74`; fx avg `0.123` n `6`; index avg `0.3226` n `23`; metal avg `2.0785` n `18`; unknown avg `2.3112` n `645`
- 4h: commodity avg `-0.8251` n `12`; crypto_alt avg `2.7202` n `228`; crypto_major avg `2.4384` n `8`; equity avg `1.2431` n `74`; fx avg `0.1259` n `6`; index avg `0.3179` n `23`; metal avg `2.0872` n `18`; unknown avg `2.2088` n `645`
- 24h: commodity avg `-1.0404` n `12`; crypto_alt avg `0.7464` n `228`; crypto_major avg `1.1775` n `8`; equity avg `1.3631` n `74`; fx avg `0.1028` n `6`; index avg `0.3912` n `23`; metal avg `2.1523` n `18`; unknown avg `1.3809` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0759`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0623`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0612`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0546`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
