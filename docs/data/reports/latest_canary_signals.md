# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-08T18:40:03.710541+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0883` n `12`; crypto_alt avg `-0.2679` n `228`; crypto_major avg `-0.1973` n `8`; equity avg `-0.1606` n `74`; fx avg `-0.0044` n `6`; index avg `-0.073` n `23`; metal avg `-0.2989` n `18`; unknown avg `0.0331` n `517`
- 1h: commodity avg `-0.0017` n `12`; crypto_alt avg `0.3616` n `228`; crypto_major avg `0.3503` n `8`; equity avg `0.1057` n `74`; fx avg `0.0097` n `6`; index avg `0.1215` n `23`; metal avg `-0.0486` n `18`; unknown avg `-0.1029` n `517`
- 4h: commodity avg `-0.209` n `12`; crypto_alt avg `0.6046` n `228`; crypto_major avg `0.229` n `8`; equity avg `0.0515` n `74`; fx avg `0.0045` n `6`; index avg `0.0275` n `23`; metal avg `0.3769` n `18`; unknown avg `-0.1665` n `517`
- 24h: commodity avg `-0.8165` n `12`; crypto_alt avg `2.5191` n `228`; crypto_major avg `2.8539` n `8`; equity avg `2.3414` n `74`; fx avg `-0.2774` n `6`; index avg `1.0907` n `23`; metal avg `-0.072` n `18`; unknown avg `-2.1069` n `506`

## Correlations

- market_context_score -> fx_forward_1h_return_pct: corr `-0.1156`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1139`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0948`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0845`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.083`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0794`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
