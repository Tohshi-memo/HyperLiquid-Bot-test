# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T00:37:35.431495+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.22` - Polymarket crypto volume is unusually high.
- 4h_commodity_crypto_divergence: score `3.9492` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0656` n `12`; crypto_alt avg `-0.2564` n `228`; crypto_major avg `-0.2283` n `8`; equity avg `-0.0362` n `74`; fx avg `0.0092` n `6`; index avg `0.0939` n `23`; metal avg `0.0885` n `18`; unknown avg `-0.079` n `645`
- 1h: commodity avg `-0.2327` n `12`; crypto_alt avg `0.1225` n `228`; crypto_major avg `0.0932` n `8`; equity avg `0.4681` n `74`; fx avg `-0.1326` n `6`; index avg `0.429` n `23`; metal avg `0.5537` n `18`; unknown avg `-0.2514` n `645`
- 4h: commodity avg `-1.0138` n `12`; crypto_alt avg `2.6669` n `228`; crypto_major avg `2.9354` n `8`; equity avg `1.5021` n `74`; fx avg `-0.0226` n `6`; index avg `0.6353` n `23`; metal avg `2.0339` n `18`; unknown avg `2.6004` n `637`
- 24h: commodity avg `-0.8502` n `12`; crypto_alt avg `1.7735` n `228`; crypto_major avg `2.1934` n `8`; equity avg `1.6828` n `74`; fx avg `-0.0302` n `6`; index avg `0.8241` n `23`; metal avg `2.1658` n `18`; unknown avg `1.5595` n `585`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1154`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0706`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0636`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0624`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
