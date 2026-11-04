# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-04T04:07:28.627181+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `4.54` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.9249` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0548` n `13`; crypto_alt avg `0.51` n `239`; crypto_major avg `0.4642` n `8`; equity avg `0.092` n `158`; fx avg `-0.0118` n `6`; index avg `0.0032` n `27`; metal avg `0.0506` n `20`; unknown avg `0.2523` n `1252`
- 1h: commodity avg `0.0139` n `13`; crypto_alt avg `0.8119` n `239`; crypto_major avg `0.9806` n `8`; equity avg `0.2673` n `158`; fx avg `-0.0135` n `6`; index avg `0.0763` n `27`; metal avg `0.0988` n `20`; unknown avg `1.207` n `1252`
- 4h: commodity avg `-0.3815` n `13`; crypto_alt avg `-1.5767` n `239`; crypto_major avg `-1.3677` n `8`; equity avg `-3.2926` n `158`; fx avg `-0.0908` n `6`; index avg `-0.5924` n `27`; metal avg `-0.2455` n `20`; unknown avg `6.1482` n `1254`
- 24h: commodity avg `-0.1888` n `13`; crypto_alt avg `0.0394` n `239`; crypto_major avg `-0.2039` n `8`; equity avg `-0.9841` n `158`; fx avg `0.1064` n `6`; index avg `-0.3522` n `27`; metal avg `-0.3598` n `20`; unknown avg `-0.4313` n `1009`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1371`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.11`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1091`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0923`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0882`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0772`, n `668`, weak_sample_signal
