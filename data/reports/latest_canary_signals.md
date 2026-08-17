# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T05:46:58.304271+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0002` n `12`; crypto_alt avg `-0.0019` n `230`; crypto_major avg `-0.0206` n `8`; equity avg `0.0446` n `114`; fx avg `-0.0115` n `6`; index avg `0.0145` n `25`; metal avg `-0.0052` n `20`; unknown avg `-0.0684` n `792`
- 1h: commodity avg `-0.0408` n `12`; crypto_alt avg `-0.1173` n `230`; crypto_major avg `-0.0666` n `8`; equity avg `0.1606` n `114`; fx avg `0.0033` n `6`; index avg `0.0328` n `25`; metal avg `0.0397` n `20`; unknown avg `-0.2918` n `792`
- 4h: commodity avg `-0.0921` n `12`; crypto_alt avg `0.4056` n `230`; crypto_major avg `0.3389` n `8`; equity avg `0.7233` n `114`; fx avg `0.0344` n `6`; index avg `0.0907` n `25`; metal avg `0.0214` n `20`; unknown avg `0.4001` n `792`
- 24h: commodity avg `-0.1842` n `12`; crypto_alt avg `0.3778` n `230`; crypto_major avg `0.6991` n `8`; equity avg `0.893` n `114`; fx avg `-0.0263` n `6`; index avg `0.1168` n `25`; metal avg `0.2135` n `20`; unknown avg `0.0527` n `759`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1735`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1479`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1433`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1214`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1164`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0959`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
