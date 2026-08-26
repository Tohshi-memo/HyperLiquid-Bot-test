# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T22:37:31.650347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `-0.1116` n `231`; crypto_major avg `-0.6002` n `8`; equity avg `0.06` n `124`; fx avg `-0.0007` n `6`; index avg `0.0245` n `25`; metal avg `0.0016` n `20`; unknown avg `0.23` n `795`
- 1h: commodity avg `-0.0213` n `12`; crypto_alt avg `0.7164` n `231`; crypto_major avg `0.4234` n `8`; equity avg `0.2802` n `124`; fx avg `-0.0098` n `6`; index avg `0.0669` n `25`; metal avg `0.1108` n `20`; unknown avg `-0.0195` n `795`
- 4h: commodity avg `-0.0023` n `12`; crypto_alt avg `1.6826` n `231`; crypto_major avg `1.2819` n `8`; equity avg `1.8144` n `124`; fx avg `-0.0142` n `6`; index avg `0.3379` n `25`; metal avg `0.1316` n `20`; unknown avg `0.3554` n `795`
- 24h: commodity avg `0.3445` n `12`; crypto_alt avg `1.0402` n `231`; crypto_major avg `0.6015` n `8`; equity avg `1.5` n `124`; fx avg `-0.0671` n `6`; index avg `0.3148` n `25`; metal avg `-0.3139` n `20`; unknown avg `0.9504` n `777`

## Correlations

- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1378`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1274`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1096`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0954`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0835`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0811`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
