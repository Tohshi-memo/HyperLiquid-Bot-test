# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-20T22:07:17.071976+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.28` n `12`; crypto_alt avg `-0.2844` n `228`; crypto_major avg `-0.2847` n `8`; equity avg `-0.2799` n `66`; fx avg `0.0022` n `6`; index avg `-0.1644` n `23`; metal avg `-0.0763` n `18`; unknown avg `0.0595` n `384`
- 1h: commodity avg `-0.2845` n `12`; crypto_alt avg `-0.5109` n `228`; crypto_major avg `-0.1721` n `8`; equity avg `-0.356` n `66`; fx avg `-0.001` n `6`; index avg `-0.1495` n `23`; metal avg `-0.0616` n `18`; unknown avg `0.02` n `384`
- 4h: commodity avg `0.3398` n `12`; crypto_alt avg `-0.3315` n `228`; crypto_major avg `-0.2137` n `8`; equity avg `-0.4236` n `66`; fx avg `-0.0377` n `6`; index avg `-0.0261` n `23`; metal avg `-0.3616` n `18`; unknown avg `-0.0247` n `384`
- 24h: commodity avg `-2.4403` n `12`; crypto_alt avg `2.6909` n `228`; crypto_major avg `1.9744` n `8`; equity avg `1.2472` n `66`; fx avg `-0.085` n `6`; index avg `1.0049` n `23`; metal avg `1.3852` n `18`; unknown avg `0.924` n `373`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0767`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0623`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0526`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0511`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0478`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0476`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0434`, n `668`, weak_sample_signal
