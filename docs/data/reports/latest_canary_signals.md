# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-12T08:07:32.304026+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.3231` n `12`; crypto_alt avg `0.4743` n `228`; crypto_major avg `0.5721` n `8`; equity avg `0.3145` n `74`; fx avg `-0.0007` n `6`; index avg `0.2357` n `23`; metal avg `0.4956` n `18`; unknown avg `-0.3375` n `643`
- 1h: commodity avg `-0.7373` n `12`; crypto_alt avg `0.4676` n `228`; crypto_major avg `0.4571` n `8`; equity avg `0.5817` n `74`; fx avg `-0.0295` n `6`; index avg `0.3115` n `23`; metal avg `0.2163` n `18`; unknown avg `0.2162` n `531`
- 4h: commodity avg `-0.5772` n `12`; crypto_alt avg `-0.2795` n `228`; crypto_major avg `-0.463` n `8`; equity avg `-0.4529` n `74`; fx avg `-0.0331` n `6`; index avg `-0.1478` n `23`; metal avg `-0.1698` n `18`; unknown avg `-0.1988` n `515`
- 24h: commodity avg `-2.358` n `12`; crypto_alt avg `1.3713` n `228`; crypto_major avg `1.4101` n `8`; equity avg `2.4059` n `74`; fx avg `-0.0347` n `6`; index avg `1.3877` n `23`; metal avg `2.2288` n `18`; unknown avg `2.0382` n `514`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0924`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0916`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0724`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0707`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.067`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.065`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0628`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0555`, n `668`, weak_sample_signal
