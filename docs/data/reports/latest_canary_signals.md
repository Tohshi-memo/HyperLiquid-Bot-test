# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T11:22:15.824711+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0411` n `12`; crypto_alt avg `-0.1817` n `228`; crypto_major avg `-0.0334` n `8`; equity avg `-0.0643` n `67`; fx avg `0.0016` n `6`; index avg `-0.0007` n `23`; metal avg `-0.1213` n `18`; unknown avg `-0.0934` n `386`
- 1h: commodity avg `0.0584` n `12`; crypto_alt avg `0.08` n `228`; crypto_major avg `0.0545` n `8`; equity avg `-0.0144` n `67`; fx avg `-0.0124` n `6`; index avg `-0.0565` n `23`; metal avg `-0.3747` n `18`; unknown avg `-0.3409` n `386`
- 4h: commodity avg `0.1535` n `12`; crypto_alt avg `-0.1869` n `228`; crypto_major avg `0.2923` n `8`; equity avg `-0.5921` n `67`; fx avg `-0.0118` n `6`; index avg `-0.1995` n `23`; metal avg `-0.0655` n `18`; unknown avg `-0.2316` n `386`
- 24h: commodity avg `-0.7702` n `12`; crypto_alt avg `2.1795` n `228`; crypto_major avg `0.85` n `8`; equity avg `1.028` n `67`; fx avg `0.0559` n `6`; index avg `0.7011` n `23`; metal avg `0.6432` n `18`; unknown avg `0.885` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0577`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0484`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0434`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0416`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0376`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0364`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0363`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0327`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.032`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0311`, n `668`, weak_sample_signal
