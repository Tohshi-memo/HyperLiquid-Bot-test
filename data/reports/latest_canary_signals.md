# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T11:07:22.020672+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.0857` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.8281` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.024` n `12`; crypto_alt avg `-0.0648` n `228`; crypto_major avg `0.0709` n `8`; equity avg `-0.1135` n `74`; fx avg `0.003` n `6`; index avg `-0.0694` n `23`; metal avg `-0.138` n `18`; unknown avg `-0.4562` n `424`
- 1h: commodity avg `-0.0837` n `12`; crypto_alt avg `-0.7071` n `228`; crypto_major avg `-0.172` n `8`; equity avg `-0.0241` n `74`; fx avg `0.0164` n `6`; index avg `0.0373` n `23`; metal avg `0.0248` n `18`; unknown avg `-0.541` n `424`
- 4h: commodity avg `-0.0022` n `12`; crypto_alt avg `1.7209` n `228`; crypto_major avg `2.0835` n `8`; equity avg `0.9503` n `74`; fx avg `0.0705` n `6`; index avg `0.2502` n `23`; metal avg `0.2554` n `18`; unknown avg `0.485` n `424`
- 24h: commodity avg `-0.447` n `12`; crypto_alt avg `-3.5695` n `228`; crypto_major avg `-1.9086` n `8`; equity avg `0.0523` n `73`; fx avg `0.1168` n `6`; index avg `0.0866` n `23`; metal avg `-0.4335` n `18`; unknown avg `-0.2835` n `402`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0994`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0937`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0814`, n `668`, weak_sample_signal
