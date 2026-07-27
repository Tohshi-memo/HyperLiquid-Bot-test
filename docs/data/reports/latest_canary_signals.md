# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-27T09:22:30.974444+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.012` n `230`; crypto_major avg `-0.0108` n `8`; equity avg `0.0224` n `100`; fx avg `-0.0092` n `6`; index avg `0.0055` n `25`; metal avg `-0.0308` n `20`; unknown avg `0.0052` n `775`
- 1h: commodity avg `-0.1625` n `12`; crypto_alt avg `-0.3439` n `230`; crypto_major avg `-0.1894` n `8`; equity avg `0.1007` n `100`; fx avg `-0.0241` n `6`; index avg `0.0345` n `25`; metal avg `0.0384` n `20`; unknown avg `-0.1432` n `775`
- 4h: commodity avg `-0.4561` n `12`; crypto_alt avg `-0.6782` n `230`; crypto_major avg `-0.337` n `8`; equity avg `0.3655` n `100`; fx avg `-0.0138` n `6`; index avg `0.046` n `25`; metal avg `0.1407` n `20`; unknown avg `-0.1173` n `759`
- 24h: commodity avg `-0.885` n `12`; crypto_alt avg `0.3283` n `230`; crypto_major avg `1.0219` n `8`; equity avg `1.4265` n `100`; fx avg `0.1089` n `6`; index avg `0.1955` n `25`; metal avg `0.4186` n `20`; unknown avg `-0.0727` n `759`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1918`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1333`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1229`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1019`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0929`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0917`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
