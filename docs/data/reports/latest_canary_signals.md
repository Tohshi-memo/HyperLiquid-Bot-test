# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T15:07:18.155021+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3654` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0335` n `12`; crypto_alt avg `0.6222` n `228`; crypto_major avg `0.5269` n `8`; equity avg `0.1037` n `67`; fx avg `-0.0062` n `6`; index avg `0.0261` n `23`; metal avg `0.0586` n `18`; unknown avg `0.0936` n `396`
- 1h: commodity avg `-0.5919` n `12`; crypto_alt avg `0.9976` n `228`; crypto_major avg `0.9699` n `8`; equity avg `0.4789` n `67`; fx avg `-0.0066` n `6`; index avg `0.2768` n `23`; metal avg `0.1149` n `18`; unknown avg `0.9042` n `396`
- 4h: commodity avg `-0.7948` n `12`; crypto_alt avg `2.0027` n `228`; crypto_major avg `1.5706` n `8`; equity avg `0.7835` n `67`; fx avg `-0.0104` n `6`; index avg `0.591` n `23`; metal avg `0.2062` n `18`; unknown avg `1.433` n `396`
- 24h: commodity avg `-0.4431` n `12`; crypto_alt avg `-3.1548` n `228`; crypto_major avg `-2.2966` n `8`; equity avg `-0.9373` n `67`; fx avg `0.0439` n `6`; index avg `0.0221` n `23`; metal avg `0.0217` n `18`; unknown avg `-2.3356` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0875`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0646`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0644`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0601`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0589`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0541`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0539`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.053`, n `668`, weak_sample_signal
