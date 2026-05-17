# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T21:52:17.587808+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5072` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `0.0188` n `12`; crypto_alt avg `-0.039` n `228`; crypto_major avg `0.0261` n `8`; equity avg `0.0523` n `65`; fx avg `-0.0038` n `5`; index avg `0.0339` n `23`; metal avg `-0.0243` n `18`; unknown avg `-0.0529` n `384`
- 1h: commodity avg `-0.0644` n `12`; crypto_alt avg `0.3154` n `228`; crypto_major avg `0.2731` n `8`; equity avg `0.0788` n `65`; fx avg `-0.0265` n `5`; index avg `0.0685` n `23`; metal avg `0.0125` n `18`; unknown avg `0.2394` n `384`
- 4h: commodity avg `-0.1108` n `12`; crypto_alt avg `0.879` n `228`; crypto_major avg `1.4066` n `8`; equity avg `0.4787` n `65`; fx avg `-0.03` n `5`; index avg `0.1888` n `23`; metal avg `-0.1006` n `18`; unknown avg `0.3647` n `384`
- 24h: commodity avg `1.6783` n `12`; crypto_alt avg `-8.8988` n `228`; crypto_major avg `-1.0896` n `8`; equity avg `-2.147` n `65`; fx avg `-0.1839` n `5`; index avg `-1.4193` n `23`; metal avg `-5.9349` n `18`; unknown avg `550.6258` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1373`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0743`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0678`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0671`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0515`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.049`, n `668`, weak_sample_signal
