# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-13T09:52:30.037960+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1762` n `12`; crypto_alt avg `-0.0676` n `228`; crypto_major avg `-0.1073` n `8`; equity avg `0.0206` n `74`; fx avg `0.0209` n `6`; index avg `-0.0025` n `23`; metal avg `0.1063` n `18`; unknown avg `0.0179` n `643`
- 1h: commodity avg `-0.1138` n `12`; crypto_alt avg `0.1678` n `228`; crypto_major avg `-0.2004` n `8`; equity avg `-0.0902` n `74`; fx avg `0.0594` n `6`; index avg `0.0061` n `23`; metal avg `0.0712` n `18`; unknown avg `0.3616` n `635`
- 4h: commodity avg `-0.197` n `12`; crypto_alt avg `1.5071` n `228`; crypto_major avg `0.7992` n `8`; equity avg `0.2076` n `74`; fx avg `-0.0204` n `6`; index avg `-0.0226` n `23`; metal avg `0.1647` n `18`; unknown avg `0.5343` n `619`
- 24h: commodity avg `0.2017` n `12`; crypto_alt avg `0.4307` n `228`; crypto_major avg `-0.404` n `8`; equity avg `-0.9301` n `74`; fx avg `0.0134` n `6`; index avg `0.5447` n `23`; metal avg `0.0651` n `18`; unknown avg `31.7686` n `611`

## Correlations

- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0855`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0853`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0787`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0745`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0592`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0586`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0551`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0524`, n `668`, weak_sample_signal
