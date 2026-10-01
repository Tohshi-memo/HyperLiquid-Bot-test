# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T21:52:33.011788+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0152` n `13`; crypto_alt avg `-0.1487` n `234`; crypto_major avg `-0.0484` n `8`; equity avg `-0.007` n `142`; fx avg `-0.0103` n `6`; index avg `0.0028` n `26`; metal avg `-0.0079` n `20`; unknown avg `-0.0431` n `945`
- 1h: commodity avg `0.1091` n `13`; crypto_alt avg `-0.7283` n `234`; crypto_major avg `-0.4531` n `8`; equity avg `-0.0808` n `142`; fx avg `0.0147` n `6`; index avg `-0.0075` n `26`; metal avg `0.0047` n `20`; unknown avg `-0.1566` n `941`
- 4h: commodity avg `0.2469` n `13`; crypto_alt avg `-1.0183` n `234`; crypto_major avg `-0.8049` n `8`; equity avg `-0.2392` n `142`; fx avg `0.055` n `6`; index avg `-0.0173` n `26`; metal avg `0.0333` n `20`; unknown avg `1.8251` n `891`
- 24h: commodity avg `0.1379` n `13`; crypto_alt avg `-0.3978` n `234`; crypto_major avg `-0.4795` n `8`; equity avg `1.0772` n `142`; fx avg `-0.1047` n `6`; index avg `0.2247` n `26`; metal avg `-0.0172` n `20`; unknown avg `-0.0357` n `816`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1165`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0907`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0891`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0828`, n `668`, weak_sample_signal
