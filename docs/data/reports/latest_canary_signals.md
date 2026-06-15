# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T09:52:32.212032+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `3.41` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `0.0071` n `12`; crypto_alt avg `0.1622` n `228`; crypto_major avg `0.2139` n `8`; equity avg `0.0063` n `74`; fx avg `0.0006` n `6`; index avg `-0.0018` n `23`; metal avg `0.0104` n `18`; unknown avg `0.0785` n `689`
- 1h: commodity avg `-0.0957` n `12`; crypto_alt avg `-0.1502` n `228`; crypto_major avg `-0.0282` n `8`; equity avg `-0.2567` n `74`; fx avg `0.0201` n `6`; index avg `-0.0764` n `23`; metal avg `0.0582` n `18`; unknown avg `0.1957` n `689`
- 4h: commodity avg `-0.4796` n `12`; crypto_alt avg `-0.0217` n `228`; crypto_major avg `0.1797` n `8`; equity avg `0.1244` n `74`; fx avg `0.0266` n `6`; index avg `0.0902` n `23`; metal avg `0.6572` n `18`; unknown avg `0.7419` n `657`
- 24h: commodity avg `-1.1818` n `12`; crypto_alt avg `2.7085` n `228`; crypto_major avg `2.8168` n `8`; equity avg `1.5452` n `74`; fx avg `0.0637` n `6`; index avg `0.9836` n `23`; metal avg `2.3296` n `18`; unknown avg `1.7867` n `529`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0718`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0626`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0599`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0581`, n `668`, weak_sample_signal
