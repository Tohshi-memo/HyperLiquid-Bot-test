# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-27T01:07:17.180250+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1506` n `12`; crypto_alt avg `0.0136` n `228`; crypto_major avg `0.0244` n `8`; equity avg `-0.055` n `67`; fx avg `-0.017` n `6`; index avg `-0.039` n `23`; metal avg `-0.1914` n `18`; unknown avg `-0.1081` n `418`
- 1h: commodity avg `-0.1972` n `12`; crypto_alt avg `0.436` n `228`; crypto_major avg `0.2679` n `8`; equity avg `-0.0617` n `67`; fx avg `-0.0234` n `6`; index avg `-0.0423` n `23`; metal avg `-0.2151` n `18`; unknown avg `0.9206` n `418`
- 4h: commodity avg `-0.5138` n `12`; crypto_alt avg `0.4425` n `228`; crypto_major avg `0.4619` n `8`; equity avg `0.1895` n `67`; fx avg `-0.0036` n `6`; index avg `0.1909` n `23`; metal avg `0.0879` n `18`; unknown avg `0.3774` n `418`
- 24h: commodity avg `0.002` n `12`; crypto_alt avg `0.1556` n `228`; crypto_major avg `-0.1724` n `8`; equity avg `0.7009` n `67`; fx avg `-0.0628` n `6`; index avg `0.9718` n `23`; metal avg `-0.1246` n `18`; unknown avg `1.4081` n `397`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1776`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1667`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1663`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1572`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.145`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1304`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1242`, n `668`, weak_sample_signal
