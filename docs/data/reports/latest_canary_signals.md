# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T20:52:49.517174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0198` n `12`; crypto_alt avg `-0.1548` n `234`; crypto_major avg `-0.0065` n `8`; equity avg `-0.141` n `142`; fx avg `-0.0054` n `6`; index avg `-0.0342` n `26`; metal avg `0.0163` n `20`; unknown avg `-0.0808` n `975`
- 1h: commodity avg `-0.035` n `12`; crypto_alt avg `0.39` n `234`; crypto_major avg `0.5476` n `8`; equity avg `-0.054` n `142`; fx avg `0.014` n `6`; index avg `-0.0247` n `26`; metal avg `0.0325` n `20`; unknown avg `-0.0336` n `889`
- 4h: commodity avg `-0.1221` n `12`; crypto_alt avg `-1.4876` n `234`; crypto_major avg `-0.6874` n `8`; equity avg `-0.2337` n `142`; fx avg `0.0037` n `6`; index avg `-0.113` n `26`; metal avg `0.057` n `20`; unknown avg `2.2321` n `889`
- 24h: commodity avg `0.3304` n `12`; crypto_alt avg `-0.1057` n `234`; crypto_major avg `0.6523` n `8`; equity avg `-0.3574` n `142`; fx avg `0.0744` n `6`; index avg `-0.0592` n `26`; metal avg `-0.2079` n `20`; unknown avg `790.4834` n `786`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1339`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1326`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1235`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1064`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.089`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.08`, n `668`, weak_sample_signal
