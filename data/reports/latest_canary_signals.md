# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-15T02:07:32.353027+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.37` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1324` n `12`; crypto_alt avg `0.0509` n `228`; crypto_major avg `-0.0043` n `8`; equity avg `-0.1085` n `74`; fx avg `0.0006` n `6`; index avg `-0.0181` n `23`; metal avg `0.1488` n `18`; unknown avg `-0.0262` n `645`
- 1h: commodity avg `-0.0956` n `12`; crypto_alt avg `0.4392` n `228`; crypto_major avg `0.2858` n `8`; equity avg `0.0293` n `74`; fx avg `0.0405` n `6`; index avg `0.0836` n `23`; metal avg `0.4938` n `18`; unknown avg `-0.398` n `637`
- 4h: commodity avg `-0.2087` n `12`; crypto_alt avg `0.789` n `228`; crypto_major avg `0.9834` n `8`; equity avg `0.2775` n `74`; fx avg `-0.0734` n `6`; index avg `0.2843` n `23`; metal avg `0.1855` n `18`; unknown avg `0.0312` n `629`
- 24h: commodity avg `-0.9386` n `12`; crypto_alt avg `1.7888` n `228`; crypto_major avg `2.1068` n `8`; equity avg `1.4283` n `74`; fx avg `0.0207` n `6`; index avg `0.7579` n `23`; metal avg `2.1453` n `18`; unknown avg `1.3444` n `577`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0944`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0785`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0744`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0642`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.054`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.052`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0507`, n `668`, weak_sample_signal
