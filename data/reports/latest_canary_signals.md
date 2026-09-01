# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-01T04:37:25.989093+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.015` n `12`; crypto_alt avg `-0.0068` n `232`; crypto_major avg `-0.0536` n `8`; equity avg `0.0223` n `130`; fx avg `-0.0048` n `6`; index avg `-0.0054` n `26`; metal avg `-0.0113` n `20`; unknown avg `-0.0837` n `792`
- 1h: commodity avg `0.0439` n `12`; crypto_alt avg `0.0052` n `232`; crypto_major avg `-0.1395` n `8`; equity avg `0.159` n `130`; fx avg `0.026` n `6`; index avg `0.0149` n `26`; metal avg `-0.0263` n `20`; unknown avg `0.436` n `790`
- 4h: commodity avg `0.0179` n `12`; crypto_alt avg `0.3483` n `232`; crypto_major avg `0.0423` n `8`; equity avg `0.1849` n `130`; fx avg `0.0174` n `6`; index avg `0.0334` n `26`; metal avg `-0.1225` n `20`; unknown avg `0.2869` n `790`
- 24h: commodity avg `0.3876` n `12`; crypto_alt avg `2.3864` n `232`; crypto_major avg `2.1006` n `8`; equity avg `1.4099` n `130`; fx avg `0.0101` n `6`; index avg `0.1104` n `26`; metal avg `-0.0474` n `20`; unknown avg `0.3707` n `751`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.102`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0553`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0532`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0504`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0488`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0485`, n `668`, weak_sample_signal
