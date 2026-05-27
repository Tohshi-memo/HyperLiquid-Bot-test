# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T07:22:15.717944+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0906` n `12`; crypto_alt avg `-0.2405` n `228`; crypto_major avg `-0.0262` n `8`; equity avg `0.0223` n `67`; fx avg `0.0081` n `6`; index avg `0.0153` n `23`; metal avg `-0.0852` n `18`; unknown avg `0.8411` n `418`
- 1h: commodity avg `-0.2216` n `12`; crypto_alt avg `0.1446` n `228`; crypto_major avg `0.33` n `8`; equity avg `0.2942` n `67`; fx avg `0.0322` n `6`; index avg `0.0337` n `23`; metal avg `-0.0953` n `18`; unknown avg `0.1109` n `418`
- 4h: commodity avg `-0.3378` n `12`; crypto_alt avg `0.0194` n `228`; crypto_major avg `0.3782` n `8`; equity avg `-0.0923` n `67`; fx avg `0.0466` n `6`; index avg `-0.2261` n `23`; metal avg `-1.0316` n `18`; unknown avg `1.1733` n `400`
- 24h: commodity avg `-0.9126` n `12`; crypto_alt avg `-0.6564` n `228`; crypto_major avg `0.2457` n `8`; equity avg `0.8206` n `67`; fx avg `0.0379` n `6`; index avg `0.7955` n `23`; metal avg `-0.7445` n `18`; unknown avg `1.7139` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1881`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1876`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1727`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1694`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1632`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.149`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1319`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1306`, n `668`, weak_sample_signal
