# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T15:01:56.876235+00:00`
- Correlation status: `ready`
- Asset price records: `656`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0966` n `12`; crypto_alt avg `-0.0206` n `228`; crypto_major avg `0.0151` n `8`; equity avg `0.1254` n `65`; fx avg `-0.0057` n `5`; index avg `0.0032` n `23`; metal avg `-0.0944` n `18`; unknown avg `-0.0169` n `375`
- 1h: commodity avg `0.3136` n `12`; crypto_alt avg `0.7139` n `228`; crypto_major avg `0.4247` n `8`; equity avg `0.1885` n `65`; fx avg `0.0033` n `5`; index avg `-0.0391` n `23`; metal avg `-0.0759` n `18`; unknown avg `0.0141` n `375`
- 4h: commodity avg `0.52` n `12`; crypto_alt avg `0.7344` n `228`; crypto_major avg `0.2662` n `8`; equity avg `1.1454` n `65`; fx avg `-0.0354` n `5`; index avg `0.4873` n `23`; metal avg `-0.2609` n `18`; unknown avg `0.1342` n `375`
- 24h: commodity avg `1.8022` n `12`; crypto_alt avg `2.382` n `228`; crypto_major avg `-0.0373` n `8`; equity avg `1.0852` n `65`; fx avg `0.2154` n `5`; index avg `0.2841` n `23`; metal avg `-0.9247` n `18`; unknown avg `0.1118` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1247`, n `648`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1214`, n `648`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.11`, n `652`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0982`, n `648`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0968`, n `648`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0945`, n `652`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0848`, n `652`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0845`, n `652`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0729`, n `652`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0728`, n `652`, weak_sample_signal
