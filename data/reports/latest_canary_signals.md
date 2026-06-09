# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-09T00:07:22.755272+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0036` n `12`; crypto_alt avg `-0.059` n `228`; crypto_major avg `-0.0131` n `8`; equity avg `-0.1345` n `74`; fx avg `0.0193` n `6`; index avg `-0.1099` n `23`; metal avg `0.0457` n `18`; unknown avg `-0.0856` n `517`
- 1h: commodity avg `-0.0074` n `12`; crypto_alt avg `-0.7901` n `228`; crypto_major avg `-0.6447` n `8`; equity avg `-0.1382` n `74`; fx avg `0.0273` n `6`; index avg `-0.1333` n `23`; metal avg `-0.216` n `18`; unknown avg `0.3215` n `517`
- 4h: commodity avg `0.0305` n `12`; crypto_alt avg `-1.1581` n `228`; crypto_major avg `-0.5101` n `8`; equity avg `-0.2182` n `74`; fx avg `0.0158` n `6`; index avg `-0.0433` n `23`; metal avg `-0.1592` n `18`; unknown avg `-0.8896` n `517`
- 24h: commodity avg `-0.6081` n `12`; crypto_alt avg `0.3306` n `228`; crypto_major avg `1.028` n `8`; equity avg `1.6168` n `74`; fx avg `-0.241` n `6`; index avg `0.6621` n `23`; metal avg `-0.4818` n `18`; unknown avg `-3.0933` n `507`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0964`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.084`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0808`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
