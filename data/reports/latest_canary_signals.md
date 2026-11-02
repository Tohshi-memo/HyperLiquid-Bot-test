# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T20:37:39.962036+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0359` n `13`; crypto_alt avg `-0.2806` n `239`; crypto_major avg `-0.2206` n `8`; equity avg `-0.6275` n `157`; fx avg `0.0009` n `6`; index avg `-0.0928` n `27`; metal avg `-0.0191` n `20`; unknown avg `30.8205` n `1262`
- 1h: commodity avg `-0.1011` n `13`; crypto_alt avg `0.193` n `239`; crypto_major avg `0.2437` n `8`; equity avg `-0.3902` n `157`; fx avg `-0.0019` n `6`; index avg `-0.0644` n `27`; metal avg `-0.0007` n `20`; unknown avg `18.3162` n `1236`
- 4h: commodity avg `-0.2858` n `13`; crypto_alt avg `-1.6211` n `239`; crypto_major avg `-1.2584` n `8`; equity avg `-2.6338` n `157`; fx avg `-0.0104` n `6`; index avg `-0.3039` n `27`; metal avg `-0.2469` n `20`; unknown avg `8.7078` n `1170`
- 24h: commodity avg `-1.3947` n `13`; crypto_alt avg `-2.9789` n `238`; crypto_major avg `-1.654` n `8`; equity avg `-3.1646` n `157`; fx avg `0.2767` n `6`; index avg `-0.0513` n `27`; metal avg `0.1878` n `20`; unknown avg `9.155` n `1016`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.171`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1678`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1647`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1592`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1173`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1126`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1119`, n `668`, weak_sample_signal
