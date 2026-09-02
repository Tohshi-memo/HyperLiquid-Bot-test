# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T16:07:31.574833+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0107` n `12`; crypto_alt avg `0.2387` n `232`; crypto_major avg `0.2872` n `8`; equity avg `0.122` n `133`; fx avg `0.0071` n `6`; index avg `0.0269` n `26`; metal avg `0.0179` n `20`; unknown avg `17.9978` n `790`
- 1h: commodity avg `0.0192` n `12`; crypto_alt avg `0.5517` n `232`; crypto_major avg `0.5408` n `8`; equity avg `0.2244` n `133`; fx avg `0.0043` n `6`; index avg `0.0386` n `26`; metal avg `-0.0405` n `20`; unknown avg `0.2948` n `789`
- 4h: commodity avg `0.415` n `12`; crypto_alt avg `0.5028` n `232`; crypto_major avg `0.7967` n `8`; equity avg `0.5244` n `133`; fx avg `-0.0837` n `6`; index avg `0.1353` n `26`; metal avg `0.2712` n `20`; unknown avg `0.389` n `789`
- 24h: commodity avg `0.7019` n `12`; crypto_alt avg `-0.9569` n `232`; crypto_major avg `-1.2178` n `8`; equity avg `-0.6204` n `133`; fx avg `-0.3233` n `6`; index avg `-0.0799` n `26`; metal avg `0.0031` n `20`; unknown avg `-0.4173` n `751`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0853`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0742`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0727`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0714`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0699`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0483`, n `668`, weak_sample_signal
