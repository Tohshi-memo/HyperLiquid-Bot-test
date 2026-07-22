# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T05:52:28.933350+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0382` n `12`; crypto_alt avg `0.0009` n `230`; crypto_major avg `-0.0652` n `8`; equity avg `0.0313` n `98`; fx avg `-0.0014` n `6`; index avg `0.0067` n `25`; metal avg `0.0274` n `20`; unknown avg `-0.0204` n `771`
- 1h: commodity avg `-0.0474` n `12`; crypto_alt avg `-0.4732` n `230`; crypto_major avg `-0.8316` n `8`; equity avg `-0.6732` n `98`; fx avg `-0.0177` n `6`; index avg `-0.1039` n `25`; metal avg `0.0626` n `20`; unknown avg `0.0734` n `771`
- 4h: commodity avg `-0.1497` n `12`; crypto_alt avg `-0.7681` n `230`; crypto_major avg `-1.1524` n `8`; equity avg `-1.405` n `98`; fx avg `0.0195` n `6`; index avg `-0.2508` n `25`; metal avg `-0.0206` n `20`; unknown avg `-0.3759` n `771`
- 24h: commodity avg `0.5822` n `12`; crypto_alt avg `-0.8111` n `230`; crypto_major avg `-1.173` n `8`; equity avg `1.264` n `98`; fx avg `0.072` n `6`; index avg `0.1414` n `25`; metal avg `0.6633` n `20`; unknown avg `0.0457` n `755`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0979`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0892`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0888`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0749`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0688`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0674`, n `666`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0636`, n `666`, weak_sample_signal
