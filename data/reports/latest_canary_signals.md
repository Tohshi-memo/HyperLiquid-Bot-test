# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-23T23:07:18.103212+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.6218` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `0.0734` n `12`; crypto_alt avg `0.1509` n `228`; crypto_major avg `0.1694` n `8`; equity avg `0.0366` n `67`; fx avg `-0.0058` n `6`; index avg `0.0618` n `23`; metal avg `0.0484` n `18`; unknown avg `-0.1828` n `396`
- 1h: commodity avg `-0.0099` n `12`; crypto_alt avg `-0.4523` n `228`; crypto_major avg `-0.1726` n `8`; equity avg `0.022` n `67`; fx avg `0.0188` n `6`; index avg `-0.1494` n `23`; metal avg `0.1254` n `18`; unknown avg `-0.0458` n `396`
- 4h: commodity avg `-1.6795` n `12`; crypto_alt avg `0.9513` n `228`; crypto_major avg `0.9423` n `8`; equity avg `0.8285` n `67`; fx avg `0.0666` n `6`; index avg `0.2292` n `23`; metal avg `0.5404` n `18`; unknown avg `0.4537` n `396`
- 24h: commodity avg `-2.7373` n `12`; crypto_alt avg `1.5648` n `228`; crypto_major avg `1.2794` n `8`; equity avg `1.5295` n `67`; fx avg `0.0446` n `6`; index avg `0.6385` n `23`; metal avg `0.7097` n `18`; unknown avg `-0.1066` n `376`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1221`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1135`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0842`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0792`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0665`, n `668`, weak_sample_signal
