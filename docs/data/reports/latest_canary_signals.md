# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T10:37:37.360933+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `0.2958` n `234`; crypto_major avg `0.222` n `8`; equity avg `0.0431` n `142`; fx avg `0.0102` n `6`; index avg `-0.003` n `26`; metal avg `0.0099` n `20`; unknown avg `1.3779` n `963`
- 1h: commodity avg `0.068` n `12`; crypto_alt avg `0.0504` n `234`; crypto_major avg `0.2691` n `8`; equity avg `-0.1002` n `142`; fx avg `0.0476` n `6`; index avg `-0.039` n `26`; metal avg `0.0068` n `20`; unknown avg `0.6658` n `961`
- 4h: commodity avg `0.1542` n `12`; crypto_alt avg `1.4635` n `234`; crypto_major avg `1.1789` n `8`; equity avg `0.0998` n `142`; fx avg `0.0727` n `6`; index avg `-0.0114` n `26`; metal avg `0.0084` n `20`; unknown avg `0.6321` n `943`
- 24h: commodity avg `-0.2876` n `12`; crypto_alt avg `0.5594` n `234`; crypto_major avg `-0.0913` n `8`; equity avg `0.0881` n `142`; fx avg `0.0375` n `6`; index avg `0.0265` n `26`; metal avg `0.1759` n `20`; unknown avg `2682.2996` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1613`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.14`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1368`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1133`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1094`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1049`, n `668`, weak_sample_signal
