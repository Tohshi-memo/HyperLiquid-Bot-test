# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-28T08:22:25.244525+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0269` n `12`; crypto_alt avg `0.0436` n `231`; crypto_major avg `0.0206` n `8`; equity avg `0.0` n `127`; fx avg `-0.0017` n `6`; index avg `-0.003` n `26`; metal avg `-0.0268` n `20`; unknown avg `-0.0061` n `792`
- 1h: commodity avg `-0.0373` n `12`; crypto_alt avg `0.0744` n `231`; crypto_major avg `0.1436` n `8`; equity avg `-0.1478` n `127`; fx avg `0.0137` n `6`; index avg `-0.0259` n `26`; metal avg `0.0528` n `20`; unknown avg `0.0195` n `792`
- 4h: commodity avg `-0.1129` n `12`; crypto_alt avg `0.028` n `231`; crypto_major avg `0.042` n `8`; equity avg `-0.4796` n `127`; fx avg `-0.0583` n `6`; index avg `-0.0658` n `26`; metal avg `0.3615` n `20`; unknown avg `0.0699` n `760`
- 24h: commodity avg `0.2848` n `12`; crypto_alt avg `-0.5501` n `231`; crypto_major avg `0.5713` n `8`; equity avg `-1.0945` n `127`; fx avg `-0.0654` n `6`; index avg `-0.0418` n `26`; metal avg `0.521` n `20`; unknown avg `0.4138` n `760`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.072`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0691`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0615`, n `668`, weak_sample_signal
