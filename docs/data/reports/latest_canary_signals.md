# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-02T00:07:30.943635+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0452` n `12`; crypto_alt avg `-0.0045` n `228`; crypto_major avg `-0.0888` n `8`; equity avg `-0.1906` n `88`; fx avg `0.012` n `6`; index avg `-0.0711` n `25`; metal avg `0.0254` n `20`; unknown avg `-0.2944` n `763`
- 1h: commodity avg `-0.056` n `12`; crypto_alt avg `-0.469` n `228`; crypto_major avg `-0.5411` n `8`; equity avg `-0.4879` n `88`; fx avg `0.0054` n `6`; index avg `-0.1581` n `25`; metal avg `-0.0379` n `20`; unknown avg `0.2718` n `763`
- 4h: commodity avg `-0.0566` n `12`; crypto_alt avg `0.0126` n `228`; crypto_major avg `-0.4149` n `8`; equity avg `-0.2602` n `88`; fx avg `0.0382` n `6`; index avg `-0.1151` n `25`; metal avg `0.0479` n `20`; unknown avg `142.4542` n `763`
- 24h: commodity avg `-0.6814` n `12`; crypto_alt avg `1.5106` n `228`; crypto_major avg `0.8277` n `8`; equity avg `-2.1755` n `88`; fx avg `0.0021` n `6`; index avg `-0.6787` n `25`; metal avg `0.3183` n `20`; unknown avg `147.7823` n `739`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1189`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1081`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1015`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1001`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0912`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0866`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0821`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0696`, n `668`, weak_sample_signal
