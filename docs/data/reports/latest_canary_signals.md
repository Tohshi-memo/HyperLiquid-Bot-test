# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T08:52:18.972465+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.2179` n `12`; crypto_alt avg `-0.4703` n `228`; crypto_major avg `-0.2276` n `8`; equity avg `-0.0459` n `67`; fx avg `-0.0181` n `6`; index avg `0.088` n `23`; metal avg `0.0812` n `18`; unknown avg `0.9023` n `418`
- 1h: commodity avg `-0.8252` n `12`; crypto_alt avg `-0.0808` n `228`; crypto_major avg `0.0351` n `8`; equity avg `0.3508` n `67`; fx avg `-0.0314` n `6`; index avg `0.286` n `23`; metal avg `0.4676` n `18`; unknown avg `0.8291` n `418`
- 4h: commodity avg `-1.0575` n `12`; crypto_alt avg `0.5721` n `228`; crypto_major avg `0.6295` n `8`; equity avg `0.4305` n `67`; fx avg `0.0106` n `6`; index avg `0.1727` n `23`; metal avg `-0.7932` n `18`; unknown avg `1.2095` n `400`
- 24h: commodity avg `-2.1506` n `12`; crypto_alt avg `-0.8821` n `228`; crypto_major avg `0.1993` n `8`; equity avg `0.9071` n `67`; fx avg `-0.0478` n `6`; index avg `1.0315` n `23`; metal avg `-0.4854` n `18`; unknown avg `1.4497` n `397`

## Correlations

- risk_on_score -> index_forward_1h_return_pct: corr `0.1856`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.182`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1716`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1687`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1635`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1268`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1239`, n `668`, weak_sample_signal
