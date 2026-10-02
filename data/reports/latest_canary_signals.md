# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T00:37:29.398713+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0095` n `13`; crypto_alt avg `-0.1618` n `234`; crypto_major avg `-0.1698` n `8`; equity avg `-0.0876` n `142`; fx avg `-0.0005` n `6`; index avg `-0.0188` n `26`; metal avg `-0.0686` n `20`; unknown avg `0.148` n `985`
- 1h: commodity avg `0.0068` n `13`; crypto_alt avg `0.3004` n `234`; crypto_major avg `-0.0003` n `8`; equity avg `0.1062` n `142`; fx avg `0.0639` n `6`; index avg `0.042` n `26`; metal avg `-0.1137` n `20`; unknown avg `-0.0114` n `977`
- 4h: commodity avg `0.0079` n `13`; crypto_alt avg `-0.0367` n `234`; crypto_major avg `-0.0407` n `8`; equity avg `0.1806` n `142`; fx avg `0.0548` n `6`; index avg `0.0323` n `26`; metal avg `-0.0582` n `20`; unknown avg `-0.2066` n `935`
- 24h: commodity avg `0.0268` n `13`; crypto_alt avg `-0.2507` n `234`; crypto_major avg `0.019` n `8`; equity avg `1.3068` n `142`; fx avg `-0.1657` n `6`; index avg `0.2297` n `26`; metal avg `0.0617` n `20`; unknown avg `0.0814` n `840`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.118`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1168`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0965`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
