# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T16:09:23.766111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1109` n `12`; crypto_alt avg `0.0929` n `228`; crypto_major avg `-0.0123` n `8`; equity avg `0.1356` n `67`; fx avg `-0.0138` n `6`; index avg `0.0969` n `23`; metal avg `0.1243` n `18`; unknown avg `-0.324` n `418`
- 1h: commodity avg `-0.0246` n `12`; crypto_alt avg `0.7624` n `228`; crypto_major avg `0.3812` n `8`; equity avg `-0.0781` n `67`; fx avg `0.0081` n `6`; index avg `-0.0209` n `23`; metal avg `0.099` n `18`; unknown avg `0.6314` n `418`
- 4h: commodity avg `0.2317` n `12`; crypto_alt avg `1.1166` n `228`; crypto_major avg `-0.0798` n `8`; equity avg `-1.1153` n `67`; fx avg `-0.0354` n `6`; index avg `-0.9644` n `23`; metal avg `0.1692` n `18`; unknown avg `0.7293` n `418`
- 24h: commodity avg `-1.0683` n `12`; crypto_alt avg `-0.5686` n `228`; crypto_major avg `-0.6887` n `8`; equity avg `-0.3753` n `67`; fx avg `-0.0576` n `6`; index avg `-0.5697` n `23`; metal avg `-1.0098` n `18`; unknown avg `0.9932` n `400`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1681`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1659`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1616`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1535`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1516`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1481`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1311`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1276`, n `668`, weak_sample_signal
