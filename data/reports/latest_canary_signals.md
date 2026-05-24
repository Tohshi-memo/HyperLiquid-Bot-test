# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T09:52:15.007294+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `70.86` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `0.0506` n `12`; crypto_alt avg `-0.0641` n `228`; crypto_major avg `0.0903` n `8`; equity avg `0.1369` n `67`; fx avg `-0.0036` n `6`; index avg `0.0051` n `23`; metal avg `-0.0076` n `18`; unknown avg `-0.0789` n `396`
- 1h: commodity avg `0.0227` n `12`; crypto_alt avg `0.2372` n `228`; crypto_major avg `0.4455` n `8`; equity avg `0.0957` n `67`; fx avg `-0.0052` n `6`; index avg `0.0146` n `23`; metal avg `-0.0403` n `18`; unknown avg `-1.0922` n `396`
- 4h: commodity avg `0.2618` n `12`; crypto_alt avg `0.5199` n `228`; crypto_major avg `0.8538` n `8`; equity avg `0.0886` n `67`; fx avg `0.0012` n `6`; index avg `0.009` n `23`; metal avg `-0.0042` n `18`; unknown avg `-0.6132` n `386`
- 24h: commodity avg `-2.7339` n `12`; crypto_alt avg `4.1219` n `228`; crypto_major avg `4.9118` n `8`; equity avg `2.6957` n `67`; fx avg `0.068` n `6`; index avg `1.3612` n `23`; metal avg `1.2661` n `18`; unknown avg `1.1802` n `386`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1151`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1143`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1141`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1098`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1033`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0897`, n `668`, weak_sample_signal
