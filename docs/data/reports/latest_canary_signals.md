# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T14:07:20.140081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0882` n `12`; crypto_alt avg `-0.3536` n `228`; crypto_major avg `-0.2712` n `8`; equity avg `-0.0794` n `67`; fx avg `0.0017` n `6`; index avg `-0.0164` n `23`; metal avg `0.0208` n `18`; unknown avg `-0.1723` n `396`
- 1h: commodity avg `0.2035` n `12`; crypto_alt avg `-0.5621` n `228`; crypto_major avg `-0.5262` n `8`; equity avg `-0.1735` n `67`; fx avg `0.0136` n `6`; index avg `-0.0403` n `23`; metal avg `-0.0762` n `18`; unknown avg `-0.0658` n `396`
- 4h: commodity avg `0.256` n `12`; crypto_alt avg `-0.9372` n `228`; crypto_major avg `-0.3855` n `8`; equity avg `0.104` n `67`; fx avg `0.0254` n `6`; index avg `-0.1325` n `23`; metal avg `-0.283` n `18`; unknown avg `0.6644` n `396`
- 24h: commodity avg `-2.2721` n `12`; crypto_alt avg `1.7824` n `228`; crypto_major avg `3.6043` n `8`; equity avg `2.376` n `67`; fx avg `0.0873` n `6`; index avg `0.972` n `23`; metal avg `1.0325` n `18`; unknown avg `1.6116` n `386`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.115`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1097`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.095`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0941`, n `668`, weak_sample_signal
