# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-24T06:22:15.249656+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0098` n `12`; crypto_alt avg `-0.0473` n `228`; crypto_major avg `-0.1474` n `8`; equity avg `-0.1997` n `67`; fx avg `0.0113` n `6`; index avg `-0.101` n `23`; metal avg `-0.0476` n `18`; unknown avg `-0.1725` n `396`
- 1h: commodity avg `-0.0437` n `12`; crypto_alt avg `0.1367` n `228`; crypto_major avg `0.0898` n `8`; equity avg `-0.1509` n `67`; fx avg `0.0051` n `6`; index avg `-0.0611` n `23`; metal avg `0.0521` n `18`; unknown avg `1.0407` n `386`
- 4h: commodity avg `-0.2247` n `12`; crypto_alt avg `-0.5359` n `228`; crypto_major avg `-0.05` n `8`; equity avg `-0.0729` n `67`; fx avg `0.0112` n `6`; index avg `-0.0098` n `23`; metal avg `0.0825` n `18`; unknown avg `0.7915` n `386`
- 24h: commodity avg `-3.0683` n `12`; crypto_alt avg `1.8077` n `228`; crypto_major avg `2.6071` n `8`; equity avg `2.2039` n `67`; fx avg `0.0473` n `6`; index avg `1.165` n `23`; metal avg `1.2414` n `18`; unknown avg `1.8348` n `386`

## Correlations

- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1267`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1181`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0939`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0913`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0775`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
