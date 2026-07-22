# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-22T15:07:27.750267+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0039` n `12`; crypto_alt avg `0.1874` n `230`; crypto_major avg `0.2289` n `8`; equity avg `0.3904` n `98`; fx avg `-0.0077` n `6`; index avg `0.0639` n `25`; metal avg `0.0421` n `20`; unknown avg `-0.1389` n `773`
- 1h: commodity avg `-0.0049` n `12`; crypto_alt avg `-0.2483` n `230`; crypto_major avg `-0.2664` n `8`; equity avg `0.0945` n `98`; fx avg `-0.0228` n `6`; index avg `0.0357` n `25`; metal avg `-0.1146` n `20`; unknown avg `0.0489` n `773`
- 4h: commodity avg `0.0369` n `12`; crypto_alt avg `0.1279` n `230`; crypto_major avg `0.0945` n `8`; equity avg `0.8521` n `98`; fx avg `-0.0252` n `6`; index avg `0.1423` n `25`; metal avg `0.1689` n `20`; unknown avg `11.7622` n `773`
- 24h: commodity avg `0.4927` n `12`; crypto_alt avg `-0.2136` n `230`; crypto_major avg `-0.9266` n `8`; equity avg `0.4222` n `98`; fx avg `-0.0371` n `6`; index avg `-0.0145` n `25`; metal avg `0.5135` n `20`; unknown avg `1.0809` n `739`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1764`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1077`, n `666`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0822`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0717`, n `666`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0693`, n `668`, weak_sample_signal
