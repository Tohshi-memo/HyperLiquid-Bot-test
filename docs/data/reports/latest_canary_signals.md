# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-21T06:52:15.355768+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1221` n `12`; crypto_alt avg `-0.046` n `228`; crypto_major avg `-0.185` n `8`; equity avg `-0.2105` n `66`; fx avg `-0.0111` n `6`; index avg `-0.0811` n `23`; metal avg `-0.1507` n `18`; unknown avg `-0.4766` n `385`
- 1h: commodity avg `0.1793` n `12`; crypto_alt avg `0.0967` n `228`; crypto_major avg `-0.2831` n `8`; equity avg `-0.2572` n `66`; fx avg `-0.0102` n `6`; index avg `-0.168` n `23`; metal avg `-0.2486` n `18`; unknown avg `-0.0327` n `375`
- 4h: commodity avg `0.2148` n `12`; crypto_alt avg `-0.3437` n `228`; crypto_major avg `-0.4117` n `8`; equity avg `-0.1516` n `66`; fx avg `0.029` n `6`; index avg `-0.0173` n `23`; metal avg `-0.3885` n `18`; unknown avg `0.0881` n `374`
- 24h: commodity avg `-1.6385` n `12`; crypto_alt avg `2.1105` n `228`; crypto_major avg `2.4405` n `8`; equity avg `1.7444` n `66`; fx avg `0.079` n `6`; index avg `1.3857` n `23`; metal avg `0.0123` n `18`; unknown avg `4.6318` n `374`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0739`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.071`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0629`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0616`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0603`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0586`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0536`, n `668`, weak_sample_signal
