# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T09:52:15.035216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0637` n `12`; crypto_alt avg `-0.1346` n `228`; crypto_major avg `-0.0995` n `8`; equity avg `0.0732` n `66`; fx avg `0.0023` n `6`; index avg `0.0707` n `23`; metal avg `0.0794` n `18`; unknown avg `-0.1883` n `384`
- 1h: commodity avg `0.2824` n `12`; crypto_alt avg `0.0244` n `228`; crypto_major avg `0.0489` n `8`; equity avg `0.0017` n `66`; fx avg `0.0107` n `6`; index avg `0.0531` n `23`; metal avg `-0.0563` n `18`; unknown avg `0.1101` n `384`
- 4h: commodity avg `-0.5385` n `12`; crypto_alt avg `0.2157` n `228`; crypto_major avg `0.3311` n `8`; equity avg `0.8227` n `66`; fx avg `-0.061` n `6`; index avg `0.4705` n `23`; metal avg `0.7821` n `18`; unknown avg `0.6435` n `374`
- 24h: commodity avg `-0.0785` n `12`; crypto_alt avg `0.5793` n `228`; crypto_major avg `0.5454` n `8`; equity avg `1.4233` n `66`; fx avg `-0.1635` n `6`; index avg `0.3136` n `23`; metal avg `-0.7427` n `18`; unknown avg `-0.0373` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0796`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0713`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0708`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0637`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0523`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0463`, n `668`, weak_sample_signal
