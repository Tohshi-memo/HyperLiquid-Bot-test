# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-24T06:52:32.426886+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0162` n `12`; crypto_alt avg `0.0676` n `228`; crypto_major avg `-0.1354` n `8`; equity avg `-0.0421` n `86`; fx avg `0.0225` n `6`; index avg `0.0076` n `23`; metal avg `-0.0493` n `20`; unknown avg `-0.1028` n `764`
- 1h: commodity avg `0.0132` n `12`; crypto_alt avg `-0.1037` n `228`; crypto_major avg `-0.0601` n `8`; equity avg `0.105` n `86`; fx avg `0.0677` n `6`; index avg `0.0363` n `23`; metal avg `0.1081` n `20`; unknown avg `-0.2252` n `748`
- 4h: commodity avg `0.0904` n `12`; crypto_alt avg `-0.0085` n `228`; crypto_major avg `0.1363` n `8`; equity avg `0.5896` n `86`; fx avg `0.1001` n `6`; index avg `0.1811` n `23`; metal avg `0.2907` n `20`; unknown avg `-0.261` n `740`
- 24h: commodity avg `-0.3634` n `12`; crypto_alt avg `-0.4232` n `228`; crypto_major avg `-1.0029` n `8`; equity avg `4.6825` n `86`; fx avg `-0.0712` n `6`; index avg `0.0724` n `23`; metal avg `-0.2169` n `20`; unknown avg `-0.2569` n `580`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1187`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.106`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0997`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.073`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0724`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0662`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0625`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0622`, n `668`, weak_sample_signal
